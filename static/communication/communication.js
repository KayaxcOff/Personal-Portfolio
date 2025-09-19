document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("#message form");
    if (form) {
        const button = form.querySelector("button[type='submit']");
        form.addEventListener("submit", async function (e) {
            e.preventDefault();

            button.disabled = true;
            button.textContent = "Sending...";

            const formData = new FormData(form);
            try {
                const response = await fetch(form.action, {
                    method: form.method,
                    body: formData,
                    headers: { 'Accept': 'application/json' }
                });
                if (response.ok) {
                    form.innerHTML = "<p style='color:lightpink;'>Thanks. Your message did send successful</p>";
                } else {
                    form.innerHTML = "<p style='color:lightpink;'>There is a bug. Please try again</p>";
                }
            } catch (error) {
                form.innerHTML = "<p style='color:lightpink;'>Wi-Fi Error!!! Please try again</p>";
            }
        });
    }
});