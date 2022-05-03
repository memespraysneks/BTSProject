document.querySelector(".week_wrap").addEventListener("click", (event) => {
    let weekid = event.target.closest(".week").dataset.weekid
    if (weekid) {
        window.location = `/week/${weekid}`
    }
})