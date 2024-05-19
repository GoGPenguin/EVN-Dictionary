from django.shortcuts import render, get_object_or_404,redirect
from .models import ListVocabulary, MyVocab
from accounts.models import UserAccount
import uuid
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def get_view_home(request):
    user_id = request.session.get('user_id')
    user = get_object_or_404(UserAccount, pk=user_id)
    user_dictionaries = ListVocabulary.objects.filter(user=user)
    
    dictionaries_info = []
    total_vocab_count = 0
    
    for dictionary in user_dictionaries:
        vocab_count = MyVocab.objects.filter(listVocab=dictionary).count()
        dictionaries_info.append({
            'list_id': dictionary.list_id,
            'list_name': dictionary.list_name,
            'vocab_count': vocab_count,
        })
        total_vocab_count += vocab_count
    
    context = {
        'user': user,
        'dictionaries_info': dictionaries_info,
        'total_vocab_count': total_vocab_count,
    }
    print(context)
    # return render(request, 'user_dictionaries.html', context)
    return render(request,'home_template.html',{'data':context})

def get_view_create_dictionary(request):
    return render(request,'create_template.html')

def handle_create(request):
    if request.method == 'POST':
        # Lấy thông tin từ form
        name_dictionary = request.POST.get('name_dictionary', '')
        vocab_data = {}
        for key, value in request.POST.items():
            if key.startswith('value_en_') or key.startswith('value_vi_'):
                vocab_data[key] = value

        # Tạo dictionary mới
        user_id = request.session.get('user_id')
        user = UserAccount.objects.get(id=user_id)
        random_uuid = uuid.uuid4()
        list_id = str(random_uuid)[:8]
        new_list = ListVocabulary.objects.create(list_id=list_id,user=user, list_name=name_dictionary)

        # Lưu từ vựng vào dictionary mới
        for key, value in vocab_data.items():
            if key.startswith('value_en_'):
                index = key.split('_')[-1]
                vocab_vn = vocab_data.get(f'value_vi_{index}')
                MyVocab.objects.create(listVocab=new_list, vocab_en=value, vocab_vn=vocab_vn)
        return redirect('/home')
    return render(request,'create_template.html')

def dictionary_detail(request,dictionary_id):
    vocabularies = MyVocab.objects.filter(listVocab__list_id=dictionary_id)

    context = {
        'dictionary_id': dictionary_id,
        'vocabularies': vocabularies,
    }
    return render(request, 'detail_dictionary_template.html', context)


def edit_dictionary(request,dictionary_id):
    dictionary = get_object_or_404(ListVocabulary, pk=dictionary_id)
    
    # Lấy tên của từ điển
    dictionary_name = dictionary.list_name
    dictionary_id = dictionary.list_id
    # Lấy tất cả các từ vựng có trong từ điển
    # vocabulary_list = MyVocab.objects.filter(listVocab=dictionary)
    vocabulary_list = MyVocab.objects.filter(listVocab=dictionary).values('myVocab_id', 'vocab_en', 'vocab_vn')
    context = {
        'dictionary_id':dictionary_id,
        'dictionary_name': dictionary_name,
        'vocabulary_list': vocabulary_list,
    }
    print(context)
    return render(request, 'edit_dictionary_template.html', context)

def handle_edit_dictionary(request):
    if request.method == 'POST':
        data = request.POST.dict()
        dictionary_id = request.POST.get('id_dictionary', '')  # Bạn cần cung cấp dictionary_id từ request
        dictionary_name = request.POST.get('name_dictionary', '')
        ListVocabulary.objects.filter(list_id=dictionary_id).update(list_name=dictionary_name)
        vocabularies = MyVocab.objects.filter(listVocab__list_id=dictionary_id)
        existing_vocab_ids = set(vocab.myVocab_id for vocab in vocabularies)
        
        # Lưu trữ các vocab_id từ data POST
        arrayId = set()
        for key, value in data.items():
            if key.startswith('value_en_') or key.startswith('value_vi_'):
                vocab_id = key.split('_')[-1]
                arrayId.add(int(vocab_id))  # Chuyển sang integer để so sánh
        

        # Xử lý update và xóa
        for vocab_id in existing_vocab_ids:
            if vocab_id not in arrayId:
                # Xoá từ vựng với vocab_id không tồn tại trong arrayId
                MyVocab.objects.filter(myVocab_id=vocab_id).delete()
            else:
                # Cập nhật giá trị cho từ vựng với vocab_id có trong arrayId
                vocab_en = data.get(f'value_en_{vocab_id}', '')
                vocab_vi = data.get(f'value_vi_{vocab_id}', '')
                MyVocab.objects.filter(myVocab_id=vocab_id).update(vocab_en=vocab_en, vocab_vn=vocab_vi)

        # Thực hiện các công việc cần thiết sau khi cập nhật hoặc xoá từ vựng
        for key, value in data.items():
            if key.startswith('addnew_en_'):
                vocab_en = value  # Lấy giá trị vocab_en mới từ data
                vocab_id = key.split("_")[-1]  # Lấy id từ chuỗi khóa
                vocab_vi = data.get(f'addnew_vi_{vocab_id}', '')  # Lấy giá trị vocab_vi mới từ data
                # Tạo mới từ vựng và thêm vào từ điển
                new_vocab = MyVocab.objects.create(listVocab_id=dictionary_id, vocab_en=vocab_en, vocab_vn=vocab_vi)
        # Redirect hoặc trả về response tùy theo logic của ứng dụng
        return redirect('/home')
        
    return render(request, 'edit_dictionary_template.html')


def delete_dictionary(request,dictionary_id):

    dictionary = get_object_or_404(ListVocabulary, pk=dictionary_id)
    
    # Xóa từ điển
    dictionary.delete()
    
    # Sau khi xóa, chuyển hướng về trang chính (home)
    return redirect('/home')


def handle_logout(request):
    logout(request)
    # Redirect hoặc trả về response tùy vào logic của ứng dụng
    return redirect('/')


def test_create(request):
    return render(request, 'test_create.html')



@csrf_exempt
def upload_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        user_id = request.session.get('user_id')
        user = UserAccount.objects.get(id=user_id)
        random_uuid = uuid.uuid4()
        list_id = str(random_uuid)[:8]
        new_list = ListVocabulary.objects.create(list_id=list_id, user=user, list_name=data['name_dictionary'])

        # Lưu từ vựng vào dictionary mới
        for item in data['data']:
            MyVocab.objects.create(listVocab=new_list, vocab_en=item['Value_en'], vocab_vn=item['Value_vi'])
        print(data)
        return JsonResponse({'message': 'Data saved successfully!'})
        # return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

    