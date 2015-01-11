# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# {{ project_name }}
# (c) 2014 ActivKonnect

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data

        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.email = data.get('email')

        if 'password1' in data:
            user.set_password(data.get('password1'))
        else:
            user.set_unusable_password()

        if commit:
            user.save()

        return user

    def add_message(self, request, level, message_template,
                    message_context=None, extra_tags=''):
        pass


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    pass
