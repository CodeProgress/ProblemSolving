//  A jar has 1000 coins.  999 are fair and 1 is double headed.
//  Pick a coin at random, and toss it 10 times.
//  Given that you see 10 heads, what is the probability that the next toss of 
//  that coin will also be heads?
//
//  Monte Carlo simulation to approximate solution:
//
//  Simulates ~20,000,000 trials per second (2014)
	  
	  
public class CondProbSim {

	public static void main(String[] args){
		
		long startTime = System.nanoTime();
		
		int numTrials = 20000000;
		int count = 0;
		int tails = 0;
		double probTenInRow = 1.0/Math.pow(2, 10);
		
		for (int i = 0; i < numTrials; i++){

			if (Math.random() < .999){
				if (Math.random() < probTenInRow){
					count += 1;
					tails += Math.round(Math.random());
				}	

			} else {
				count += 1;
			}
		}
		
		System.out.println(1 - tails/Double.valueOf(count));
		
		long timeInNano = System.nanoTime() - startTime;
		double timeInSeconds = timeInNano * Math.pow(10, -9);
		System.out.println("Elapsed time in seconds: " + timeInSeconds);

	}
}
