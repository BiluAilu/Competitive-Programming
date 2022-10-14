int select(int arr[], int i)
	{
		int min = i;  
        for (int j = i + 1; j < arr.length; j++){  
            if (arr[j] < arr[min]){  
            	min = j;
            }  
        } 
        return min;
	}

	void selectionSort(int arr[], int n)
	{
		for (int i = 0; i < arr.length; i++)
		{
			int j = select(arr, i);
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}