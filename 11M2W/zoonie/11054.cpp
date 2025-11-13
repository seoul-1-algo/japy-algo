#include <iostream>
#include <algorithm>
using namespace std;

int arr[1000];
int dp[1000];
int dp2[1000];
int ans1 = 0;
int ans2 = 0;
int ans3 = 0;
int main()
{
	int n;
	cin>>n;
	for(int i=0; i<n; i++)
	{
			cin>>arr[i];
	}	
	
	for(int i=0; i<n; i++)
	{
		dp[i]=1;
		for(int j=0; j<i; j++)
		{
			if(arr[i]>arr[j])
			{
				dp[i]=max(dp[i],dp[j]+1);
			}
		
		}
			
		ans1 = max(ans1, dp[i]);
	}	
	
	for(int i = n-1; i >= 0; i--)
	{
        dp2[i] = 1;
        for(int j = n-1; j > i; j--)
		{
            if(arr[i] > arr[j])
			{
                dp2[i] = max(dp2[i],dp2[j] + 1);
			}	
		}
			
		ans2 = max(ans2, dp2[i]);
	}
	
	for(int i =0; i<n; i++)
	{
		ans3 = max(ans3, dp[i]+dp2[i]-1);
	}
	cout<<ans3<<endl;
}
	
	
	
