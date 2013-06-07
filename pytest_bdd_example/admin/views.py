

@bp.route('/')
def index(template='dashboatd.html'):

    if not current_user.is_authenticated():
        template = "login.html"

    return render_template(template)
