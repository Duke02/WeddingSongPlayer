use crate::api::api_defs::{index, translate};
use rocket::routes;

pub(crate) mod api;

#[rocket::main]
async fn main() -> Result<(), Box<rocket::Error>> {
    let _rocket = rocket::build()
        .mount("/", routes![index, translate])
        .launch()
        .await?;
    Ok(())
}
