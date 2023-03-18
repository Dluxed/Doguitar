var rowIndex = document.getElementById("rowIndex");
var acordes = document.getElementById("chordButtons");


const chordsNatural = ["C", "D", "E", "F", "G", "A", "B"];

//Seleccion de acordes
for(let i=0; i < 7; i++){
    console.log(chordsNatural[i]);
    acordes.innerHTML += "<a href='" + chordsNatural[i] + "' class='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded'>"+ chordsNatural[i] +"</a>";
}


//MUESTRA EL ACORDE EN EL DIAPASON
for(let i=0; i < 13; i++){
    rowIndex.innerHTML += "<span class='w-4'>" + i + "<span>";
}



