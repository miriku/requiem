#!/usr/bin/perl

# helper function that takes virus RNA file A and B amd merges them to virus C
sub crossPollinate
{
  ($Avirus, $Bvirus, $Cvirus) = @_;
  open( RHA, $Avirus );
  open( RHB, $Bvirus );
  open( RHC, ">", $Cvirus );

  # we start with no virus being read at start
  $readAhead = 0;

  # 60 base pairs per line, 153 lines
  # for each line
  for( my $i = 0; $i < 1; $i++ )
  {
    my $A = <RHA>;
    my @A = split //, $A;
    my $B = <RHB>;
    my @B = split //, $B;
    my @C;

    # for each base pair
    for( my $j = 0; $j < 153*60; $j++ )
    {
      # are we done copying last batch? if so figure out which virus we read from
      if( $readAhead == 0 )
      {
        # time to find out which file we will read, or if we will mutate
        my $chance = int(rand(3));
        if( $chance == 0 )
        {
          # mutate
          # mutation pushes one base pair then exits loop
          my $randomData = (int(rand(4)));
          if( $randomData == 0 ) { $randomData = "a"; }
          elsif( $randomData == 0 ) { $randomData = "c"; }
          elsif( $randomData == 0 ) { $randomData = "g"; }
          else { $randomData = "t"; }
          push( @C, $randomData );
          next;
        }
        elsif( $chance == 1 )
        {
          # read virus A
          $readAhead = int(rand(500));
          $currentlyReading = "A";
        }
        else
        {
          # read virus B
          $readAhead = int(rand(500));
          $currentlyReading = "B";
        }
      }

      # we are now guaranteed a non-zero readAhead
      if( $currentlyReading eq "A" )
      {
        push( @C, $A[$j]);
      }
      else
      {
        push( @C, $B[$j]);
      }

      $readAhead--;
    }

    # write line to disk
    print RHC @C;
    print RHC "\n";
  }

  close( RHA );
  close( RHB );
  close( RHC );
}

crossPollinate( "1", "32", "16" );
crossPollinate( "1", "16", "8" );
crossPollinate( "1", "8", "4" );
crossPollinate( "1", "4", "2" );
crossPollinate( "2", "4", "3" );
crossPollinate( "4", "8", "6" );
crossPollinate( "4", "6", "5" );
crossPollinate( "6", "8", "7" );
crossPollinate( "8", "16", "12" );
crossPollinate( "8", "12", "10" );
crossPollinate( "8", "10", "9" );
crossPollinate( "10", "12", "11" );
crossPollinate( "12", "16", "14" );
crossPollinate( "12", "14", "13" );
crossPollinate( "14", "16", "15" );
crossPollinate( "16", "32", "24" );
crossPollinate( "16", "24", "20" );
crossPollinate( "16", "20", "18" );
crossPollinate( "16", "18", "17" );
crossPollinate( "18", "20", "19" );
crossPollinate( "20", "24", "22" );
crossPollinate( "20", "22", "21" );
crossPollinate( "22", "24", "23" );
crossPollinate( "24", "32", "28" );
crossPollinate( "24", "28", "26" );
crossPollinate( "24", "26", "25" );
crossPollinate( "26", "28", "27" );
crossPollinate( "28", "32", "30" );
crossPollinate( "28", "30", "29" );
crossPollinate( "30", "32", "31" );
