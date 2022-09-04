const {DateTime} = require("luxon");

module.exports = function(eleventyConfig) {
    
    // making copy of directories in the output public folder
    eleventyConfig.addPassthroughCopy("./src/style.css");
    eleventyConfig.addPassthroughCopy("./src/assets");

   
    let markdownIt = require("markdown-it");
    let markdownItKatex = require("@iktakahiro/markdown-it-katex");
    let options = {
        html: true
    };
    let markdownLib = markdownIt(options)
    markdownLib.use(markdownItKatex);
    
    eleventyConfig.setLibrary("md", markdownLib);
    
    
    // Adding some math config 
    // let markdownIt = require("markdown-it");
    // let markdownItKatex = require("@iktakahiro/markdown-it-katex");
    // let options = {
    //     html: true,
    //     breaks: true,
    //     linkify: true,
    //   };
    // let md = new markdownIt(options);
    // md.use(markdownItKatex);
    
    // let markdownLib = markdownIt(options).use(markdownItKatex);
    //eleventyConfig.setLibrary("md", markdownLib);
    
    // eleventyConfig.addFilter("markdown", (content) => {
        
    //     return md.render(content);
    //     });
    

    // Adding function for dates
    eleventyConfig.addFilter("postDate", (dateObj) => {
        return DateTime.fromJSDate(dateObj).toLocaleString(DateTime.DATE_FULL)
    });

    return {
        dir: {
            input: "src",
            output: "public"
        }
    }
}