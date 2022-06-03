// Write Javascript code here
const request = require('request');
const cheerio = require('cheerio');
const fs = require('fs');


const URL = "https://www.bol.com/nl/nl/v/art-craft/1359759/";

request(URL, function(err, res, body) {
    if (err) {
        console.log(err);
    } else {
        const $ = cheerio.load('ul.fluid-grid--m')
        console.log($.html())
            // console.log(body)
    }
});