// #[macro_use] extern crate rocket;

use rocket::get;
use rocket::serde::json::Json;
use serde_derive::{Deserialize, Serialize};

#[get("/")]
pub fn index() -> &'static str {
    "Hello, world!"
}

#[get("/translate/<to_translate>")]
pub fn translate(to_translate: &str) -> String {
    // TODO: Actually make this use AI (wow!)
    to_translate.to_owned()
}

#[derive(Debug, Serialize, Deserialize)]
pub enum Language {
    // TODO: Add songs that you expect to have in your playlist.
    English,
    Spanish,
    Japanese,
    French,
    Other(String)
}


#[get("/detect_language/<words>")]
pub fn detect_language(words: &str) -> Json<Language> {
    if !words.is_empty() {
        Json(Language::English)
    } else {
        Json(Language::Spanish)
    }

}
