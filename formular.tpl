<!DOCTYPE html>
<html lang="en">
<head>
    <title>Synchronizer</title>
    <meta charset="utf-8"></meta>
    <meta name="viewport" content="width=device-width, initial-scale=1"></meta>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css"></link>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>
<br></br>
<div class="container">
    <div class="jumbotron">
        <h2 class='text-center'>Synchronize Campus Virual with your Google Calender</h2><br></br>
        <form class="form-horizontal" action="/" method="post">
            <div class="form-group">
                <p>You need to enter your credentials of your Campus Virtual account and your Google account to get this
                    application working</p>
                <p>The credentials of your Campus Virtual account : </p>
                <label class="control-label col-sm-2" for="email">Username:</label>
                <div class="col-sm-10">
                    <input type="email" class="form-control" id="email" placeholder="Enter email" name="userNameCampus"></input>
                </div>
            </div>
            <div class="form-group">
                <label class="control-label col-sm-2" for="pwd">Password:</label>
                <div class="col-sm-10">
                    <input type="password" class="form-control" id="pwd" placeholder="Enter password"
                           name="pwdCampus"></input>
                </div>
            </div>
            <div class="form-group">
                <p>The credentials of your Google account : </p>
                <label class="control-label col-sm-2" for="email">Username:</label>
                <div class="col-sm-10">
                    <input type="email" class="form-control" id="email2" placeholder="Enter email" name="email"></input>
                </div>
            </div>
            <div class="form-group">
                <label class="control-label col-sm-2" for="pwd">Password:</label>
                <div class="col-sm-10">
                    <input type="password" class="form-control" id="pwd2" placeholder="Enter password"
                           name="pwd"></input>
                </div>
            </div>
            <div class="form-group">
                <div class="text-right">
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-success">Submit</button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>
</body>
</html>