from boston_order_ivr import create_app, db
app = create_app("development")

with app.app_context():
    from boston_order_ivr.base.models import LandingUpdate
    landing_updates = [
        {
            "language": "english",
            "label": "English",
            "body": """Text Goes Here!

##Markdown

<strong>AND HTML</strong> is safe."""
        },
        {
            "language": "arabic",
            "label": "عربى",
            "body": "Text Goes Here!"
        },
        {
            "language": "farsi",
            "label": "فارسی",
            "body": "Text Goes Here!"
        },
        {
            "language": "somali",
            "label": "Somali",
            "body": "Text Goes Here!"
        }
    ]
    for x in landing_updates:
        lu = LandingUpdate()
        lu.language = x["language"]
        lu.label = x["label"]
        lu.body = x["body"]
        db.session.add(lu)
    db.session.commit()
