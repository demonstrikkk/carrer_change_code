//document.getElementById("test-button").addEventListener("click", async () => {
//    try {
//        const response = await fetch("http://127.0.0.1:5000/test-post", {
//            method: "POST",
//            headers: {
//                "Content-Type": "application/json"
//            },
//            body: JSON.stringify({ test_key: "test_value" })
//        });
//        const result = await response.json();
//        console.log(result);
//        alert(`Response: ${JSON.stringify(result)}`);
//    } catch (error) {
//        alert(`Error: ${error.message}`);
//    }
//});
//


document.getElementById('career-form').addEventListener("submit", async (event) => {
    event.preventDefault();

    // Mapping of form fields (HTML IDs) to real field names
    const fieldMapping = {
        field_study: 'Field of Study',
        current_occupation: 'Current Occupation',
        age: 'Age',
        gender: 'Gender',
        years_of_experience: 'Years of Experience',
        education_level: 'Education Level',
        industry_growth: 'Industry Growth Rate',
        job_satisfaction: 'Job Satisfaction',  // Job Satisfaction is constant
        work_life_balance: 'Work-Life Balance',
        job_opportunities: 'Job Opportunities',
        job_security: 'Job Security',
        career_change: 'Career Change Interest',
        skills_gap: 'Skills Gap',
        family_influence: 'Family Influence',
        mentorship: 'Mentorship Available',
        certifications: 'Certifications',
        freelancing: 'Freelancing Experience',
        mobility: 'Geographic Mobility',
        professional_networks: 'Professional Networks',
        technology_adoption: 'Technology Adoption',
        salary_group: 'Salary Group'
    };

    const inputData = {};

    // Set job_satisfaction to true always
    inputData['Job Satisfaction'] = true;

    for (const [htmlId, fieldName] of Object.entries(fieldMapping)) {
        const element = document.getElementById(htmlId);

        // Ensure the element exists
        if (!element) {
            console.error(`Element with ID ${htmlId} not found.`);
            continue;
        }

        // Handle checkbox type input
        if (element.type === 'checkbox') {
            inputData[fieldName] = element.checked;
        }
        // Handle range or number inputs
        else if (element.type === 'range' || element.type === 'number') {
            inputData[fieldName] = parseInt(element.value, 10) || 0;  // Default to 0 if NaN
        }
        // Handle other inputs (text, select, etc.)
        else {
            inputData[fieldName] = element.value.trim() !== ""
                ? (isNaN(element.value) ? element.value : parseInt(element.value, 10))
                : ""; // Default empty string for empty fields
        }
    }

    try {
//        console.log(inputData)
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputData)
        });

        if (!response.ok) {
            throw new Error('Failed to fetch prediction');
        }

        const result = await response.json();
        alert(`Prediction Result: ${result.prediction}`);
    } catch (error) {
        console.error('Error:', error);
        alert(`Error: ${error.message}`);
    }
});
