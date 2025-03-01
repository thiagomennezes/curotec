"use client";

import { useState, useEffect } from "react";
import axios from "axios";

export default function Customers() {
  const [customers, setCustomers] = useState([]);
  const [newCustomer, setNewCustomer] = useState({ name: "", email: "", person_id: "" });
  const [editCustomer, setEditCustomer] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);
  const limit = 3;

  const API_URL = "http://127.0.0.1:8020/customers/";

  useEffect(() => {
    fetchCustomers();
  }, [page]);

  const fetchCustomers = async () => {
    setLoading(true);
    try {
      const response = await axios.get(API_URL, { params: { skip: (page - 1) * limit, limit } });
      setCustomers(response.data);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  const addCustomer = async () => {
    if (!newCustomer.name || !newCustomer.email || !newCustomer.person_id) {
      alert("All fields are required");
      return;
    }
    try {
      const response = await axios.post(API_URL, newCustomer);
      fetchCustomers();
      setNewCustomer({ name: "", email: "", person_id: "" });
    } catch (err) {
      setError(err.message);
    }
  };

  const updateCustomer = async () => {
    if (!editCustomer || !editCustomer.name || !editCustomer.email || !editCustomer.person_id) {
      alert("All fields are required");
      return;
    }
    try {
      await axios.put(`${API_URL}${editCustomer.id}/`, editCustomer);
      fetchCustomers();
      setEditCustomer(null);
    } catch (err) {
      setError(err.message);
    }
  };

  const deleteCustomer = async (id) => {
    try {
      await axios.delete(`${API_URL}${id}/`);
      fetchCustomers();
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Customers</h1>
      {loading && <p>Loading...</p>}
      {error && <p className="text-red-500">Error: {error}</p>}
      
      <div className="my-4">
        <input
          type="text"
          placeholder="Name"
          value={newCustomer.name}
          onChange={(e) => setNewCustomer({ ...newCustomer, name: e.target.value })}
          className="border p-2 mr-2"
        />
        <input
          type="email"
          placeholder="Email"
          value={newCustomer.email}
          onChange={(e) => setNewCustomer({ ...newCustomer, email: e.target.value })}
          className="border p-2 mr-2"
        />
        <input
          type="text"
          placeholder="Person ID"
          value={newCustomer.person_id}
          onChange={(e) => setNewCustomer({ ...newCustomer, person_id: e.target.value })}
          className="border p-2 mr-2"
        />
        <button onClick={addCustomer} className="bg-blue-500 text-white p-2">Add</button>
      </div>
      
      {editCustomer && (
        <div className="my-4">
          <h2 className="text-lg font-bold">Edit Customer</h2>
          <input
            type="text"
            placeholder="Name"
            value={editCustomer.name}
            onChange={(e) => setEditCustomer({ ...editCustomer, name: e.target.value })}
            className="border p-2 mr-2"
          />
          <input
            type="email"
            placeholder="Email"
            value={editCustomer.email}
            onChange={(e) => setEditCustomer({ ...editCustomer, email: e.target.value })}
            className="border p-2 mr-2"
          />
          <input
            type="text"
            placeholder="Person ID"
            value={editCustomer.person_id}
            onChange={(e) => setEditCustomer({ ...editCustomer, person_id: e.target.value })}
            className="border p-2 mr-2"
          />
          <button onClick={updateCustomer} className="bg-green-500 text-white p-2">Update</button>
        </div>
      )}
      
      <ul>
        {customers.map((customer) => (
          <li key={customer.id} className="border p-2 my-2 flex justify-between">
            <span>{customer.name} - {customer.email} - {customer.person_id}</span>
            <div>
              <button onClick={() => setEditCustomer(customer)} className="bg-yellow-500 text-white p-2 mx-1">Edit</button>
              <button onClick={() => deleteCustomer(customer.id)} className="bg-red-500 text-white p-2">Delete</button>
            </div>
          </li>
        ))}
      </ul>
      
      <div className="mt-4">
        <button onClick={() => setPage(page - 1)} disabled={page === 1} className="bg-gray-300 p-2 mr-2">Previous</button>
        <span>Page {page}</span>
        <button onClick={() => setPage(page + 1)} className="bg-gray-300 p-2 ml-2">Next</button>
      </div>
    </div>
  );
}

