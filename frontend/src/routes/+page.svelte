<script>
  import { useState } from 'svelte';
  import axios from 'axios';
  import { navigate } from 'svelte-routing';  // Used for navigation to the dashboard

  let firstName = '';
  let lastName = '';
  let turfName = '';
  let errorMessage = '';

  const handleSubmit = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/owners/login', {
        params: {
          first_name: firstName,
          last_name: lastName,
          turf_name: turfName
        }
      });

      if (response.data.length > 0) {
        // Successful login, redirect to the dashboard
        navigate('/dashboard');
      } else {
        // If no matching owner found
        errorMessage = 'Owner not found or invalid credentials.';
      }
    } catch (error) {
      errorMessage = 'Error while checking credentials, please try again later.';
    }
  };
</script>

<style>
  .login-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #45a049;
  }

  .error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
  }
</style>

<div class="login-container">
  <h2>Login</h2>
  <form on:submit|preventDefault={handleSubmit}>
    <input
      type="text"
      bind:value={firstName}
      placeholder="First Name"
      required
    />
    <input
      type="text"
      bind:value={lastName}
      placeholder="Last Name"
      required
    />
    <input
      type="text"
      bind:value={turfName}
      placeholder="Turf Name"
      required
    />
    <button type="submit">Login</button>
  </form>

  {#if errorMessage}
    <p class="error-message">{errorMessage}</p>
  {/if}
</div>
