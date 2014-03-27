
import java.util.Arrays;

class MaxProfit{
	public static void main(String args[]){

		int numValues = 10;
		
		int[] stockPrices = new int[numValues];
		
		for (int i = 0; i < stockPrices.length; i++){
			int quote = (int) (Math.random() * numValues);
			
			stockPrices[i] = quote;
			
		}
		
		System.out.println(Arrays.toString(stockPrices));
		
		System.out.println(maxProfit(stockPrices));
		
	}
	
	public static int maxProfit(int[] stockPrices){
		//Takes an array and prints the max profit if indices are buy/sell opportunities/values
		
		if (stockPrices.length == 0){
			return -1;
		}
		if (stockPrices.length == 1){
			return 0;
		}
		
		int minPrice = stockPrices[0];
		int maxProf  = 0;
		
		for (int i = 1; i < stockPrices.length; i++){
			int curVal = stockPrices[i];
			if (curVal < minPrice){
				minPrice = curVal;
			}else{
				if (curVal - minPrice > maxProf){
					maxProf = curVal - minPrice;
				}
			}
		}
		
		return maxProf;
	}
}

