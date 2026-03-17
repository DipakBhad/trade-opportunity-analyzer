def analyze_with_gemini(sector, news_data):
    try:
        from google import genai

        client = genai.Client(api_key="YOUR_API_KEY")

        prompt = f"""
Analyze the {sector} sector based on this news:

{news_data}

Give output in clean markdown format:

# {sector.title()} Sector Analysis

## 📊 Market Overview
(2-3 lines)

## 🚀 Opportunities
- point 1
- point 2
- point 3

## ⚠️ Risks
- point 1
- point 2

## ✅ Conclusion
(1-2 lines)
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        # ✅ MARKDOWN FALLBACK (IMPORTANT)
        return f"""
# {sector.title()} Sector Analysis

## 📊 Market Overview
The {sector} sector is growing steadily with strong demand.

## 🚀 Opportunities
- High investment potential  
- Innovation growth  
- Expanding market  

## ⚠️ Risks
- Market competition  
- Regulatory challenges  

## ✅ Conclusion
The {sector} sector shows promising trade opportunities.
"""