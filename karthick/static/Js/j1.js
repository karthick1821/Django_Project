


function login()
{
    var username=document.getElementById("name").value;

    var password=document.getElementById("pass").value;
   if (username==="admin" && password==="admin@123")
   {

      alert("Login Succerssfully");
      window.location="{% url 'Home'%}";
      
   }
   else
   {
      alert("Invalid Username and Password")
   }
}