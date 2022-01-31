![analog_css_logo](https://user-images.githubusercontent.com/73239367/151891399-547444bb-d4de-4b2d-9597-18fbeb800356.png)


# AnalogCSS
#### A programatic CSS utility framework to generate dynamic utility classes on the fly, without clouding up your stylesheet or markup.

# Quick and basic usage instructions:
Download the code from this repo: https://github.com/Jammin-Coder/AnalogCSS/archive/refs/heads/main.zip  
Unzip the `AnalogCSS-main.zip` folder, after it's extracted you should have an `AnalogCSS-main` folder. Open that folder and copy all of the contents into a directory of your choice.  
There is a `.html` file inside of that directory, open it up in a code editor of your choice, and also open it in a web browser. As you can see, it's just a basic HTML document with a couple headers and some divs. Now it's time to style!!  
As you can see at the top of the HTML file, we are linking to 2 CSS files, one is called `analog.css`, and one is called `app.css`. `analog.css` is the CSS file to which the program outputs generated CSS, and is not for you to write your styles in, lest they be deleted when the program runs. You can create any styles you want in `app.css`. NOTE: The order in which the CSS files are linked to makes a differance in deciding which styles should be applyed if there are confilcting styles being applyed to the same element. If you want all of the `analog.css` classes to have prevalence over the classes you write in `app.css`, then make sure to link to `app.css` AFTER linking to `analog.css`.  



## Run the program
To make AnalogCSS watch your HTML file, run `python analog_css.py`. This will start AnalogCSS, and thus will monitor your HTML files for new styles to generate.  
At the moment, there are no styles, so...

### Apply Analog styles.
The generale syntax of an AnalogCSS class is `[breakpoint:]<property>=<value>`, where `[breakpoint:]` is an optional breakpoint, `<property>` is the name of the CSS property which you are tergeting, and `<value>` is the value of the property. 
If you are confused, read on! If you're not confused, you should still read on!  

In the `body` tag of the HTML file, add this class to it: `p=2` (you can replace `2` with whatever number you want, even decimals or fractions), then refresh the page.  
You will notice the entire page now has a padding of `2rem`.  

# Understanding how it works.
There is a JSON file, `analog_config.json`, and in that file there is a JSON object called `class_mappings`. In this object, there are more objects  
with names of your choice, and those names are mapped to properties.  
```json
"p": {
  "property": "padding",
  "unit": "rem"
}
```
For example In the class name you entered in the `body` tag, it says `p=`. AnalogCSS reads this class name, and determines that `p` means `padding`  
since the `"property"` key of `"p"` is mapped to `"padding"`. It also knows to use `rem` as the unit becuase the `"unit"` key is mapped to `"rem"`.  
The program then extracts the value that you assigned to `p`, and evaluates that it should be `2rem`. After that, this information is used to generate a CSS class with the name of `.p\=2` and the property of `padding: 2rem;`. If there is no corresponding class for the property, the program will read it as a litteral css property. For example if I made a class in my markup called `display=flex`, the program woud generate a class called `display\=flex` and have the attribute be `display: flex;`.  
Regardless of the property type, this class is then written to `analog.css` and now the browser can apply it's styles.  
Note there is a backslash(`\`) in the name becuase an eqals (`=`) is a special character, and not usually supposed to be used for class names. In this case it's OK since we don't have to ever work with or look at the contents of `analog.css`.  

If you would like to apply the same value to 2 properties, for example setting the `padding-left` and `padding-right` of an element to the same value, you can supply the propertie names in an array in the `property` field of the shorthand class object, like this:  
```json
"px": {
    "property": ["padding-left", "padding-right"],
    "unit": "rem"
}
```  
This will allow you to use the `px=<some-number>` class to apply padding to the side of elements.  

### What if you want to apply styles with different units?
Not a problem at all! You can specify a unit directly in the class name! Like this:
```html
<div class="p=2em"></div>
```  
Since `em` is appended to the value, the program will know to use `em` instead of `rem`. You don't even need to specify a `"unit"` field in the classes JSON object, so long as the value you provide to the class name is a valid value for the corresponding class.

## Breakpoints
To use breakpoints in AnalogCSS, simply prepend one of the following breakpoints to your AnalogCSS class:
`xs`,  
`sm`,  
`md`,  
`lg`,  
`xl`   
followed by a colon (`:`) like this:  
```html
<div class="m=0.5em sm:m=1em"></div>
```
Assuming there is an `"m"` object for `margin` in the `"class_mappings"`, this will generate a class that sets the margin of the element to `0.5em` when the screen is below the small (`sm`) breakpoint, but once the screen's width is greater than the small breakpoint, it will have a margin of `1em`.  
The breakpoints are defined in the `"breakpoints"` object in `analog_config.json`.  
If you would like to use a breakpoint without adding it to `"breakpoints"`, the simply prepend `@breakpoint-value:` to your class name, like this:  
```html
<div class="m=0.5em @400px:m=1em">
  Below 400px I have a margin of 0.5em, but greater than 400px I have a margin of 1em.
</div>
``` 
This will yeild a similar result to using the `sm` breakpoint, but you can change the breakpoint directly in your markup.  

### Applying your own classes at specific breakpoints
Say you have a class in your own CSS file (`app.css` or other) that changes an element's theme to dark when the screen reaches the large breakpoint:  
```css
.dark-mode {
  background-color: #333;
  color: white;
}
```
Instead of writing a media query for this, you could just do this:  
```html
<div class="lg:dark-mode">
  I go to the dark side if the screen is bigger than the supplied breakpoint!
</div>
``` 
Again, you can use custom breakpoint values for this.

# More documentation to come!
Feel free star and watch this repository if you are interested in following the development of this framework, as I plan to work on it frequently!
