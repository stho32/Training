const fs   = require("fs");
const path = require("path");

const script_path = __dirname;
const data_path   = path.join(script_path, "../data");

const arguments = process.argv.slice(2);
if (arguments.length != 2) {
    console.log("you can use the following commands:");
    console.log("  - book list - list all books");
    return;
}

const maincommand = arguments[0];
const subcommand  = arguments[1];

if (maincommand == "book" && subcommand == "list") 
{
    let books = JSON.parse(fs.readFileSync(path.join(data_path, "books.json") , 'utf8'));

    books.forEach((book) => {
        console.log(book.title);
    });
}


