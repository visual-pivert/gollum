from flask import Flask, Blueprint, render_template, request, redirect, url_for
from domain.account.adapters.AccountAdapter import AccountAdapter
from domain.account.AccountEntity import AccountEntity
from domain.account.forms.CreateAccountForm import CreateAccountForm
from kink import di
from domain.account.IAccount import IAccount

account_app = Blueprint('account_app', __name__, template_folder="./templates")


@account_app.route("/account", methods=['POST', 'GET'])
def createAccount():
    # injection de dependance
    account = di[IAccount]

    form = CreateAccountForm(request.form)
    if "POST" == request.method and form.validate():
        new_account = AccountEntity()
        new_account.username = form.username.data
        new_account.email = form.email.data
        new_account.password = form.password.data
        account.createAccount(new_account)
        return redirect(url_for('index'))
    return render_template("account.html", form=form)
