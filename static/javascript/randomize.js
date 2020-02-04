var contents=new Array()
contents[0]='<input type="radio" name="option" value="option1"> {{ question.option1 }} <br>'
contents[1]='<input type="radio" name="option" value="option1"> {{ question.option1 }} <br>'
contents[2]='<input type="radio" name="option" value="option1"> {{ question.option1 }} <br>'
contents[3]='<input type="radio" name="option" value="option1"> {{ question.option1 }} <br>'

var i=0
//variable used to contain controlled random number
var random
var spacing="<br>"
//while all of array elements haven't been cycled thru
while (i<contents.length){
    //generate random num between 0 and arraylength-1
    random=Math.floor(Math.random()*contents.length)
    //if element hasn't been marked as "selected"
    if (contents[random]!="selected"){
        document.write(contents[random]+spacing)
        //mark element as selected
        contents[random]="selected"
        i++
    }
}