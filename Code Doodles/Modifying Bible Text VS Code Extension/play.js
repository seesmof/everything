async function getVerse() {
  const translation = "KJV";
  const baseUrl = "https://bible-api.com/";
  const query = `${baseUrl}?random=verse&translation=${translation}`;

  try {
    const response = await fetch(query);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("An error occurred:", error);
    throw error;
  }
}

getVerse()
  .then((data) => {
    console.log(data.text);
    console.log(data.reference);
  })
  .catch((error) => {
    console.error("An error occurred:", error);
  });
