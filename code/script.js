const fromText = document.querySelector(".from-text"),
toText = document.querySelector(".to-text"),
exchageIcon = document.querySelector(".exchange"),
selectTag = document.querySelectorAll("select"),
icons = document.querySelectorAll(".row i");
translateBtn = document.querySelector("button");

selectTag.forEach((tag, id) => {
    for (let country_code in countries) {
        let selected = id == 0 ? country_code == "fi" ? "selected" : "" : country_code == "hi" ? "selected" : "";
        let option = `<option ${selected} value="${country_code}">${countries[country_code]}</option>`;
        tag.insertAdjacentHTML("beforeend", option);
    }
});


    
fromText.addEventListener("keyup", () => {
    if(!fromText.value) {
        toText.value = "";
    }
});

translateBtn.addEventListener("click", () => {
    let text = fromText.value.trim(),
    translateFrom = selectTag[0].value,
    translateTo = selectTag[1].value;
    if(!text) return;
    toText.setAttribute("placeholder", "Translating...");
    let apiUrl = `https://translation.googleapis.com/language/translate/v2?key=AIzaSyA1Uf8ZIg4GlvoLLA1r56BVHS6BTg7umO8&q=${text}&source=${translateFrom}&target=${translateTo}`;
    fetch(apiUrl).then(res => res.json()).then(data => {
        toText.value = data.data.translations[0].translatedText;
        toText.setAttribute("placeholder", "Translation");
    }).catch(error => {
        console.error(error);
        toText.setAttribute("placeholder", "Error occurred");
    });
});



