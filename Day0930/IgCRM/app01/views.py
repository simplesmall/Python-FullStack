from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

# Create your views here.
def login(request):
    if request.is_ajax():
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        validate=request.POST.get("validate")
        response={"user":None,"err_msg":""}
        if validate.upper()==request.session.get('keep_str').upper():
            return HttpResponse("OK")
        else:
            response["err_msg"]="验证码错误"
            return JsonResponse(response)
    else:
        return render(request,"login.html")

def get_valid_img(request):

    # 方式1: 读取指定图片
    # with open("static/img/valid.jpg","rb")as f:
    #     data=f.read()

    # 方式2:基于PIL模块创建验证码图片
    from  PIL import  Image,ImageDraw,ImageFont
    from io import BytesIO

    def get_random_color():
        import random
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # img=Image.new("RGB",(350,46),get_random_color())
    # f=open("valid.png","wb")
    # img.save(f)
    # with open("valid.png","rb")as f:
    #     data=f.read()

    # 方式3:直接存储到内存上
    # img=Image.new("RGB",(350,38),get_random_color())
    # f=BytesIO()
    # img.save(f,"png")
    # data=f.getvalue()

    # 方法4:完善文本
    # img = Image.new("RGB", (350, 38), get_random_color())
    # draw=ImageDraw.Draw(img)
    # draw.text((0,0),"Python web",get_random_color())
    # # 写与读
    # f = BytesIO()
    # img.save(f, "png")
    # data = f.getvalue()

    # 方法5:动态变动数字
    img = Image.new("RGB", (350, 38), get_random_color())
    draw = ImageDraw.Draw(img)
    font=ImageFont.truetype("static/font/LCD.ttf",32)

    import random
    global  keep_str

    keep_str=""
    for i in range(6):
        random_num=str(random.randint(0,9))
        random_lowalp=chr(random.randint(97,122))
        random_upperalp=chr(random.randint(65,90))
        random_char=random.choice([random_num,random_lowalp,random_upperalp])

        draw.text((i*40+32, 0), random_char, get_random_color(),font=font)
        keep_str+=random_char

    # 甚至可以写点干扰项
    width=350
    height=38
    for i in range(4):
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw.line((x1,y1,x2,y2),fill=get_random_color())

    for i in range(20):
        draw.point([random.randint(0,width),random.randint(0,height)],fill=get_random_color())
        x= random.randint(0,width)
        y=random.randint(0,height)
        draw.arc((x,y,x+4,y+4),0,90,fill=get_random_color())
    # 写与读
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()

    print('keep str::',keep_str)

    # 将验证码存放在各自的session中
    request.session['keep_str']=keep_str
    return HttpResponse(data)
