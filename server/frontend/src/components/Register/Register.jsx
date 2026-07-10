import React, { useState } from 'react';
import "./Register.css";
import Header from '../Header/Header';

const Register = () => {

  const [userName, setUserName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const register_url = window.location.origin + "/djangoapp/register/";

  const register = async (e) => {
    e.preventDefault();

    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName: userName,
        firstName: firstName,
        lastName: lastName,
        email: email,
        password: password
      }),
    });

    const json = await res.json();

    if (json.status === "Authenticated" || json.userName != null) {
      alert("Registration successful");
      window.location.href = "/login";
    }
    else {
      alert("Registration failed");
    }
  };

  return (
    <div>
      <Header />

      <form className="login_panel" onSubmit={register}>

        <div>
          <span className="input_field">Username </span>
          <input
            type="text"
            className="input_field"
            placeholder="Username"
            onChange={(e)=>setUserName(e.target.value)}
          />
        </div>

        <div>
          <span className="input_field">First Name </span>
          <input
            type="text"
            className="input_field"
            placeholder="First Name"
            onChange={(e)=>setFirstName(e.target.value)}
          />
        </div>

        <div>
          <span className="input_field">Last Name </span>
          <input
            type="text"
            className="input_field"
            placeholder="Last Name"
            onChange={(e)=>setLastName(e.target.value)}
          />
        </div>

        <div>
          <span className="input_field">Email </span>
          <input
            type="email"
            className="input_field"
            placeholder="Email"
            onChange={(e)=>setEmail(e.target.value)}
          />
        </div>

        <div>
          <span className="input_field">Password </span>
          <input
            type="password"
            className="input_field"
            placeholder="Password"
            onChange={(e)=>setPassword(e.target.value)}
          />
        </div>

        <div>
          <input className="action_button" type="submit" value="Register"/>
        </div>

      </form>

    </div>
  );
};

export default Register;
