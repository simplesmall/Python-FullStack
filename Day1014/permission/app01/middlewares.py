from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        current_path = request.path
        # 设置白名单放行
        # 校验是否登录
        user_id=request.session.get("user_id")
        if not user_id:
            return redirect("/login/")
        # 校验权限
        import re
        permission_list = request.session.get("permission_list")
        for reg in permission_list:
            reg="^%s$"%reg
            ret = re.search(reg,current_path)
            if ret:
                return None
        return HttpResponse("无访问权限")
        if current_path in ["/login/"]:
            return None
