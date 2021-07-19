from flask import Blueprint, current_app, render_template, request

bp = Blueprint('primonator', __name__, url_prefix='/primonator')


@bp.route("/")
def item():
    url = current_app.config['PRIMO_URL']
    aleph_link = request.args.get('aleph_link')
    aleph_id = permalink_to_id(aleph_link)
    alma_id = aleph_id_to_alma_id(aleph_id)
    alma_link = alma_id_to_link(alma_id, url)

    return render_template("primonator_form.html",
                           aleph_link=aleph_link,
                           aleph_id=aleph_id,
                           alma_id=alma_id,
                           alma_link=alma_link)


def permalink_to_id(aleph_link):
    if aleph_link is None:
        return None

    id = aleph_link.split('/')[-1]
    return id


def aleph_id_to_alma_id(aleph_id):
    if aleph_id is None:
        return None

    return f'alma99{aleph_id}0106761'


def alma_id_to_link(alma_id, url):
    if alma_id is None:
        return None

    return f'{url}{alma_id}'
