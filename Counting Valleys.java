    public static int countingValleys(int steps, String path) {
    // Write your code here
    int sum = 0;
    int valley = 0;
    
    for (int i = 0; i < steps; i++)
    {
        if (path.charAt(i) == 'U')
        {
            sum++;
            if (sum == 0)
            {
                valley++;
            }
        }
        else
        {
            sum--;
        }
    }
    return (valley);

    }