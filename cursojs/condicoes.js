/** 
var c = 1
while (c <= 10){
    console.log(`passo ${c}`)
    c++
}
*/


for(var c = 1;c <= 11;c++){
    if (c >= 1 && c <= 9) {
        mes = '0' + c;
        mes2 = '0' + (c+1);
        if (c <= 9){
            mes2 = (c+1);            
        }
    } else {
        mes = c;
        mes2 = c+1;
    }
    var data = '01'+'-'+mes+'-'+'2020';
    var data2 = '01'+'-'+mes2+'-'+'2020';
    console.log(data,data2)

}
