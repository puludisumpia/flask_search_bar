(function() {
    let search = document.querySelector("#search")
    let results = document.querySelector("#results")
    let search_term = ""

    fetch(`${window.origin}/api/articles/all/`)
        .then(response => {
            if (response.ok){
                return response.json()
            }
        })
        .then(articles => {
            let showList = () => {
                results.innerHTML = ""
                articles.filter((article) => {
                    return (
                        article.title.toLowerCase().includes(search_term) || 
                        article.content.toLowerCase().includes(search_term)
                    )
                })
                .forEach((e) => {
                    const a = document.createElement("a")
                    
                    a.innerHTML = `<h5>${e.title}</h5>`
                    let lien = `${window.origin}/article/${e.id}/`
                    a.setAttribute("href", lien)
                    results.appendChild(a)
                });
            }

            showList()

            search.addEventListener("input", (event) => {
                search_term = event.target.value.toLowerCase()
                showList()
            })
        })

        .catch((error) => {
            console.log(error)
        })
})()