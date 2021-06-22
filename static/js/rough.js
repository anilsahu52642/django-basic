// //document.write..
document.write('<h1>document.write...</h1>')
document.write('<h3>used to write inside page(documnet)...we can use any html tag also</h3>')
document.write('for this line i am not using any tag')
document.write('<i><u><b><h3>here i am using italic,bold,underline,h3 and hr tags to print this line </h3></b></u></i><hr>')


// //// single line comment in javascript is // and muti line comment is /*  */


// // //varibles in javascript(3 types var,let,const)...
document.write('<h1>varibles in javascript(3 types var,let,const)</h1>')
document.write('<h3>var<br>')
document.write('we can use these format for varible(firstname,first_name,first-name,firstName,firstname23) othewise error of invalid:inexpected token</h3>')
var firstname='one variable'
document.write(firstname,"<br>")
firstname='reassigning varible'
document.write(firstname,'.....(no need to use var during reassigning )<br>')
firstname=true
document.write(firstname,"<br>")
var secondname
document.write(secondname,"<br>")
secondname='second variable';
document.write(secondname)



// // //.....................................................................
// // // events in javascript.......
document.write('<hr><h1>Events in javascript...</h1><br>')
document.write("<button onclick='hello()' name='button' id='anilbutton2'>click me</button><br>");
document.write("<span ondblclick=hello()>Double click here</span><br>")
document.write("<span oncontextmenu=hello()>Right click here</span><br>")
document.write("<span onmouseover=hello()>Drag mouse here</span><br>")
document.write("<span onmouseout=hello()>Drag mouse and take out from here</span><br>")
document.write("<span onmouseup=hello()>Click and hold for few second and release</span><br>")
document.write("<span onmousedown=hello()>Click and hold for few second</span><br>")
document.write("<span onkeypress=hello()>Type something in the keyboard ..it works inside body or inside forms see code written inside body of html</span><br>")
document.write("<span onresize=hello()>Resize the browser window ..it works inside body.. see code written inside body of html</span><br>")
document.write("<span onscroll=hello()>works if more text are inside page and we are using scroll(up down or left right)..it works inside body.. see code written inside body of html</span><br>")


function hello(){
  alert('hello how are you');
}
