# Z++

## Questions

1.
#y is to be subtracted from x
function subtract(x,y)
{
    $z <- add(x,-y)
    return($z)
}

2.

function multiply($x,$y)
{
    while($y)
    {
        $ans <- add($ans,$x)

        $y <- subtract($y,1)
    }

    return($ans)
}

3.
function multiply($x,$y)
{
    if($y)
    {
        $ans <- add($ans,$x)

        $y <- subtract($y,1)

        multiply($x,$y)
    }

    return($ans)
}



## Debrief

1. None

2. 30min
