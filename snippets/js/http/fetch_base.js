const response = await fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data) // body data type must match "Content-Type" header
});
response.json(); 
