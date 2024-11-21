<script>
    import { onMount } from "svelte";
    let message = "";
  
    onMount(async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/test/"); // Django API URL
        if (response.ok) {
          const data = await response.json();
          message = data.message;
        } else {
          message = `Error: ${response.status} ${response.statusText}`;
        }
      } catch (error) {
        message = `Error: ${error.message}`;
      }
    });
  </script>
  
  <main>
    <h1>API Response</h1>
    <p>{message}</p>
  </main>
  