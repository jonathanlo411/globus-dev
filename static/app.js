
// Init API method
document.querySelector('#auth').addEventListener('click', async () => {
    let rawRes = await fetch('/api/auth')
    let res = await rawRes.json()
    console.log(res)
})
document.querySelector('#search').addEventListener('click', async () => {
    let rawRes = await fetch('/api/search')
    let res = await rawRes.json()
    console.log(res)
})