// #[macro_use] extern crate rocket;

use rocket::get;

#[get("/")]
pub fn index() -> &'static str {
    "Hello, world!"
}

#[get("/translate/<to_translate>")]
pub fn translate(to_translate: &str) -> String {
    to_translate.to_owned()
}
