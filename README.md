# Analog CSS

An awesome CSS preprocessor to keep your CSS DRY. [Github Repo](https://github.com/Jammin-Coder/AnalogCSS)  

![analog_css_logo.png](https://timbattblog.com/images/resource/061422-62a8c3ba2ba84)

## What is it?
*Analog CSS* is a CSS preprocessor that allows you to create 'template' CSS classes. The template classes accept "parameters" that can be used inside of the class.
The values of the parameters are determined when they are "called" in the user's markup.  
Here's an example. You have a template class in `templates.scss`:  
```
.m-#{margin} {
    margin: #{margin}rem;
}
```

This template expects a value after `m-`, and that value is the amount of margin to be applied the the element.
So, in your markup if you have a `div` with a class of `m-2`, Analog CSS will determine that you want that `div` to have a margin of 2rem, based on the template class you defined, and the value given to the class when you "called" it.



## Some usage examples:

First, download this repository's code, and copy the `analog-css` directory into a project directory of your choice. Then, in your project directory, define a template class in `templates.scss`:

```scss
// template.scss

// Create a template class that accepts a value in the #{margin} parameter
.m-#{margin} {
    // use #{margin} to access the value passed in to the #{margin} parameter
    margin: #{margin}rem;
}
```

Then in your markup, you can use this template class to define actual CSS classes:

```html
<!-- index.html -->

<div class='m-1'>
    I have a margin of one!
</div>

<div class='m-2'>
    I have a margin of 2 rem!
</div>
```

Then run the Analog pre-processor:  
```
dart run analog-css/bin/analog.dart
```

That will monitor all HTML, PHP, SCSS, and CSS files and check for new class names and
template classes. The preprocessor will then read your template files and your markup files, and determine that there should be 2 classes generated, one called `.m-1` and the other `.m-2`. It also determins the value that was passed into the class name, in this case `1` and `2`, and uses those values to give the generated class its apropriate margin:


```css
/* analog.css */

.m-1 {
    margin: 1rem;
}

.m-2 {
    margin: 2rem;
}
```



The generated classes are dependent upon the classes you use in your markup.
You can use this same pattern for creating and generating classes of all sorts.


```SCSS
// templates.scss

// Resulting class will change the font-size of the element to #{fontSize} rem.
.font-#{fontSize} {
    font-size: #{fontSize}rem;
}

// Resulting class will give the element a blue background whos lightness/darkness is determined by #{scale}.
.bg-blue-#{scale} {
    background-color: hsl(245, 100%, #{scale}%);
}

// Resulting class will provide #{marginX} rem of margin to the left and right of the container.
.mx-#{marginX} {
    margin: 0 #{marginX}rem;
}

// Resulting class will provide #{marginY} rem of margin to the top and bottom of the container.
.my-#{marginY} {
    margin: #{marginY}rem 0;
}

```

Note, the parameters in template class names must be separated by a `-`:
```scss
// Allowed:
.grid-container-#{width}-#{bg}
```
```scss
// NOT ALLOWED:
.grid-container#{width}#{bg}
```