from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

TOURS = [
  {"category":"Budget", "title":"7-Day Sri Lanka Highlights (Budget)", "duration":"7 Days",
   "desc":"Sigiriya • Kandy • Nuwara Eliya • Ella • Yala • Galle", "price_note":"Best value plan"},
  {"category":"Adventure", "title":"Adventure + Hikes", "duration":"5–7 Days",
   "desc":"Mandaram Nuwara • Ella hikes • waterfalls • safari options", "price_note":"For active travelers"},
  {"category":"Family", "title":"Family-Friendly Sri Lanka", "duration":"6–8 Days",
   "desc":"Easy travel pace • kid-friendly stops • safe stays • flexible days", "price_note":"Comfort + fun"},
]

GALLERY = [
    {"src": "/static/images/gallery/01.png", "alt": "Pinnawala elephant orphanage"},
    {"src": "/static/images/gallery/02.png", "alt": "Hill country views"},
    {"src": "/static/images/gallery/03.png", "alt": "Beach and sunset"},
    {"src": "/static/images/gallery/05.png", "alt": "Galle fort coast"},
    {"src": "/static/images/gallery/04.png", "alt": "Tea plantation walk"},
    {"src": "/static/images/gallery/06.png", "alt": "Train ride experience"},
]

@app.get("/gallery", response_class=HTMLResponse)
def gallery(request: Request):
    return templates.TemplateResponse(
        "gallery.html",
        {"request": request, "images": GALLERY}
    )


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tours": TOURS}
    )

@app.get("/tours", response_class=HTMLResponse)
def tours(request: Request):
    return templates.TemplateResponse(
        "tours.html",
        {"request": request, "tours": TOURS}
    )

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "sent": False})

@app.post("/contact", response_class=HTMLResponse)
def contact_submit(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
):
    # For now: just print. Next step: send email via SendGrid/Mailgun/Gmail API.
    print(f"[Inquiry] name={name} email={email} message={message}")

    return templates.TemplateResponse(
        "contact.html",
        {"request": request, "sent": True, "name": name}
    )

