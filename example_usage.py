from client import VirtualTryOnFitProfileAttributeMatcherClient

def main():
    client = VirtualTryOnFitProfileAttributeMatcherClient()
    res = client.match_virtual_try_on_fit({'height_cm': 180, 'chest_cm': 102})
    print('Virtual Try-On Fit Matcher: ' + res['vto_match_id'] + ' (Size: ' + res['recommended_size'] + ')')
    print('Confidence: ' + str(res['fit_confidence_score_pct']) + '% | Verdict: ' + res['projected_fit_verdict'])
    print('VTO URL: ' + res['vto_dossier_telemetry_url'])

if __name__ == '__main__':
    main()
