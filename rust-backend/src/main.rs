use crate::api::api_defs::{detect_language, index, translate};
use rocket::routes;

pub(crate) mod api;

#[rocket::main]
async fn main() -> Result<(), Box<rocket::Error>> {
    let _rocket = rocket::build()
        .mount("/", routes![index, translate, detect_language])
        .launch()
        .await?;
    Ok(())
}
