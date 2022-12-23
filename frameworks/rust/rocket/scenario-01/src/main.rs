#[macro_use] extern crate rocket;

#[get("/hello?<name>")]
fn index(name: &str) -> String {
    format!("Hello {}", name)
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/api", routes![index])
}