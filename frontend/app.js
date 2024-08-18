document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("userForm");
  const responseDiv = document.getElementById("response");

  form.addEventListener("submit", async (event) => {
    event.preventDefault(); // Previene el comportamiento por defecto del formulario (recarga de la página)

    const formData = new FormData(form);

    const data = {
      username: formData.get("username"),
      email: formData.get("email"),
      password: formData.get("password"),
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/users/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const jsonResponse = await response.json();
        responseDiv.innerHTML = `<p>User created: ${JSON.stringify(
          jsonResponse
        )}</p>`;
      } else {
        responseDiv.innerHTML = `<p>Error: ${response.statusText}</p>`;
      }
    } catch (error) {
      responseDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
  });
});
