import matplotlib.pyplot as plt

def main():
    issue_types = ['API Issue', 'Login Issue', 'Report Generation', 'Data Import', 'Feature Request', 'Billing Issue', 'UI Bug']
    frequencies = [5, 6, 5, 11, 6, 10, 7]

    plt.figure(figsize=(8, 6))
    plt.pie(frequencies, labels=issue_types, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Issue Types')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the chart to a file
    plt.savefig('issue_distribution.png')
    plt.close()

    print("Issue Distribution chart generated.")

    agents = ['A001', 'A002', 'A003', 'A004', 'A005']
    avg_resolution_times = [2.8, 3.1, 2.5, 3.0, 2.7] #Example Data in Days
    avg_satisfaction = [4.3, 4.6, 4.1, 4.4, 4.5] #Example Data (1-5 scale)

    plt.figure(figsize=(10, 6))
    plt.scatter(avg_resolution_times, avg_satisfaction, s=[100, 150, 120, 110, 130], c=['red','green','blue','orange','purple']) #Size and color for better visualization
    plt.title('Agent Performance: Resolution Time vs. Customer Satisfaction')
    plt.xlabel('Average Resolution Time (Days)')
    plt.ylabel('Average Customer Satisfaction (1-5)')

    for i, agent in enumerate(agents):
        plt.annotate(agent, (avg_resolution_times[i], avg_satisfaction[i]))

    plt.grid(True)

    # Save the chart to a file
    plt.savefig('agent_performance.png')
    plt.close()

    print("Agent Performance chart generated.")

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    avg_satisfaction = [4.2, 4.5, 4.1, 4.3, 4.6, 4.4] #Example data

    plt.figure(figsize=(10, 6))
    plt.bar(months, avg_satisfaction, color='purple') #Or use plt.plot for a line chart
    plt.title('Average Customer Satisfaction Over Past Months')
    plt.xlabel('Month')
    plt.ylabel('Average Satisfaction Rating (1-5)')
    plt.ylim(0, 5)  # Set y-axis limits to 0-5
    plt.grid(axis='y')

    # Save the chart to a file
    plt.savefig('customer_satisfaction.png')
    plt.close()

    print("Customer Satisfaction chart generated.")