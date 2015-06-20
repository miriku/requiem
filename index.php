<html>
<head>
  <style>
    body {
      background-color: black;
      face: "Monaco";
    }

    h1 {
      color: White;
      font-family: "Futura"
    }

    h3 {
      color: White;
      font-family: "Futura"
    }

    a:link, a:active, a:visited {
      font-family: "Futura";
      color: Black;
      text-decoration: none;
    }

    span {
      display: inline-block;
      white-space: nowrap;
      height: 40px;
      width: 40px;
      line-height: 40px;

      -moz-border-radius: 20px;
      border-radius: 20px;

      background-color: white;
      text-align: center;
    }

    .this {
      background-color: darkred;
    }

    .stayTop {
      position: fixed;
    }

    .left{
    float:left;
    width:16%;
    overflow:hidden;
    }

    .spacer{
      float:left;
      width:5%;
      overflow:hidden;
    }

    .smallSpacer{
      float:left;
      width:2%;
      overflow:hidden;
    }

    .right{
    float:left;
    width:38%;
    overflow:hidden;
    }

    .farRight{
    float:left;
    width:39%;
    overflow:hidden;
    }
  </style>
</head>
<body>
<table width='100%' cellspacing="0" border="0" cellpadding="40">
  <tr>
    <td>
      <h1>
        REQUIEM 32
      </h1>

      <h2>
        <?php
          $current = $_GET["i"];
          if( $current == "" or $current == 0)
          {
            $current = 1;
          }

          print "<p>";

          for( $i = 1; $i < 33; $i++ )
          {
            if( $i == $current )
            {
              print "<a href=\"index.php?i=$i\"><span class='this'>$i</span></a> ";
            }
            else {
              print "<a href=\"index.php?i=$i\"><span>$i</span></a> ";
            }
          }
          print "</p>";
        ?>

      </h2>
      <div class="left">
        <br>
        <div class="stayTop">
          <h3>
            GUIDE
          </h3>
          <?php
            require( "guide.html" );
          ?>
        </div>
      </div>

      <div class="spacer">
        &nbsp;
      </div>

      <div class="right">
        <br>
        <?php
          $i = $_GET["i"];
          if( $i == "" or $i == 0)
          {
            $i = 1;
          }
        ?>
        <h3>
          GENOTYPE <?php print "$i"; ?>
        </h3>
        <?php
          require( "html/$i.html" );
        ?>
      </div>

      <div class="smallSpacer">
        &nbsp;
      </div>

      <div class="farRight">
        <br>
        <h3>
          REQUIEM <?php print "$i"; ?>
        </h3>
        <audio controls autoplay>
          <source src=<?php print "\"mp3/".$i?>.mp3" type="audio/mpeg">
        </audio>
        <br><br>
        <?php
          $file1 = "png/" . $i . "a.png";
          $file2 = "png/" . $i . "b.png";
          if( file_exists($file1)) { print "<img src=$file1 width=100% height=62%>"; }
          if( file_exists($file2)) { print "<br><br><img src=$file2 width=100% height=62%>"; }
        ?>
      </div>
    </td>
  </tr>
</table>
