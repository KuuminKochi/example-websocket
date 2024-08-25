<script>
    let result = null

    async function testPost() {
        fetch('./hello')
        .then(d => d.text())
        .then(d => (result = d))
    }

</script>

<html lang="en">
    <body>
        <button type="button" class="button" on:click={testPost}>
        test
        </button>
        {result}
    </body>
</html>

<style>
    body {
        display: flex;
        justify-content: center;
        width: 100%;
        height: 100%;
    }

    .button {
        border: solid black 2px;
        padding: 10px;
    }
</style>



