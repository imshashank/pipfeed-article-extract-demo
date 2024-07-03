import csv

# List of example URLs
urls = [
    "https://www.cnn.com/2021/07/14/world/tusimple-autonomous-truck-spc-intl/index.html",
    "https://www.cnn.com/2021/05/12/world/ironhand-exoskeleton-glove-spc-intl/index.html",
    "https://www.cnn.com/2021/06/15/asia/swarm-robots-hong-kong-warehouse-hnk-spc-intl/index.html",
    "https://www.cnn.com/2022/03/15/investing/brics-emerging-markets-russia/index.html",
    "https://www.cnn.com/2022/03/15/business/russia-europe-sanctions-energy/index.html",
    "https://www.cnn.com/2022/03/15/europe/ukraine-protester-interrupts-russian-state-news-broadcast/index.html",
    "https://www.cnn.com/2022/03/14/media/fox-correspondent-ben-hall-ukraine/index.html",
    "https://www.cnn.com/2022/03/14/investing/russia-economy-default/index.html",
    "https://www.cnn.com/2022/03/14/energy/oil-prices/index.html",
    "https://www.cnn.com/2022/03/14/energy/india-russia-oil/index.html",
    "https://www.cnn.com/2022/03/15/investing/japan-crypto-exchanges-russia-sanctions-intl-hnk/index.html",
    "https://www.cnn.com/2022/03/14/business/potassium-iodide-pills-demand-surge/index.html",
    "https://www.cnn.com/2022/03/12/tech/russia-internet-censorship-circumvention/index.html",
    "https://www.cnn.com/2022/03/14/tech/meta-guidance-heads-of-state/index.html",
    "https://www.cnn.com/2022/03/14/investing/citi-russia/index.html",
    "https://www.cnn.com/2022/03/02/business/companies-pulling-back-russia-ukraine-war-intl-hnk/index.html",
    "https://www.cnn.com/2022/03/11/tech/russia-internet-backbone-cogent-lumen/index.html",
    "https://www.cnn.com/2022/03/15/business/britain-cost-of-living/index.html",
    "https://www.cnn.com/2022/03/15/business-food/starbucks-cup-sustainability/index.html",
    "https://www.cnn.com/2022/03/14/economy/china-jan-feb-economy-challenges-ahead-intl-hnk/index.html",
    "https://www.cnn.com/2022/03/14/business/hong-kong-covid-economy-inequality-intl-hnk-mic/index.html",
    "https://www.cnn.com/2022/03/14/tech/shenzhen-lockdown-foxconn-operations-intl-hnk/index.html",
    "https://www.cnn.com/2022/03/14/economy/yield-curve-bonds-recession/index.html",
    "https://www.cnn.com/2022/03/14/economy/federal-reserve-biden-bloom-raskin/index.html",
    "https://www.cnn.com/2022/03/15/business/climate-shell-fossil-fuel-energy-intl/index.html",
    "https://www.cnn.com/2022/03/14/energy/energy-vault-renewable-storage-spc-intl/index.html",
    "https://www.cnn.com/2022/03/14/business/ford-gm-eliminate-options-chip-shortage/index.html",
    "https://www.cnn.com/2022/03/14/cars/tesla-cruise-control/index.html",
    "https://www.cnn.com/2022/03/14/tech/nasa-roscosmos-international-space-station-mark-vande-hei-scn/index.html",
    "https://www.cnn.com/2022/03/14/tech/pete-davidson-blue-origin-launch-scn/index.html",
    "https://www.cnn.com/2022/03/03/investing/india-cryptocurrency-investing-future-hnk-intl/index.html",
    "https://www.cnn.com/2022/02/01/investing/india-budget-digital-rupee/index.html",
    "https://www.cnn.com/2021/11/02/business/adar-poonawalla-risk-takers/index.html",
    "https://www.cnn.com/2021/09/09/tech/india-software-saas-intl-hnk/index.html",
    "https://www.cnn.com/2022/03/12/business/russia-diamonds-sanctions/index.html",
    "https://www.cnn.com/2022/03/11/tech/ukraine-neon-chips/index.html",
    "https://www.cnn.com/2022/03/08/business/nickel-prices-electric-vehicles/index.html",
    "https://www.cnn.com/2022/03/01/business/wheat-prices-russia-ukraine/index.html",
    "https://www.cnn.com/2022/03/12/business/food-crisis-ukraine-russia/index.html",
    "https://www.cnn.com/2021/07/15/business/whim-app-helsinki-spc-intl/index.html",
    "https://www.cnn.com/2021/10/26/tech/seatrec-bedrock-robot-seabed-mapping-climate-spc-hnk/index.html",
    "https://www.cnn.com/2022/03/15/health/covid-rising-uk-us/index.html",
    "https://www.cnn.com/2022/03/13/health/pandemic-year-three-predictions/index.html",
    "https://www.cnn.com/2022/03/13/health/pfizer-vaccine-4th-dose/index.html",
    "https://www.cnn.com/2022/03/11/health/covid-endemic-pandemic-anniversary-america-patient-gupta/index.html",
    "https://www.cnn.com/2022/03/10/health/covid-community-levels-cdc/index.html",
    "https://www.cnn.com/2022/02/08/entertainment/academy-award-nominations/index.html",
    "https://www.cnn.com/2022/03/15/golf/cameron-smith-wins-players-championship-spt-intl/index.html",
    "https://www.cnn.com/2022/03/15/sport/karl-anthony-towns-minnesota-timberwolves-spt-intl/index.html",
    "https://www.cnn.com/2022/03/15/sport/brooklyn-nets-fined-kyrie-irving-locker-room-spt-intl/index.html",
    "https://www.cnn.com/2022/03/15/motorsport/lewis-hamilton-change-name-mother-f1-spt-intl/index.html",
    "https://www.cnn.com/2022/03/14/sport/brittney-griner-arrest-russia-jonathan-franks-cmd-spt-intl/index.html",
    "https://www.cnn.com/2022/03/14/football/messi-neymar-what-next-psg-spt-intl/index.html",
    "https://www.cnn.com/2022/03/14/sport/mlb-pete-alonso-mets-car-crash-spt/index.html",
    "https://www.cnn.com/2022/03/14/golf/shane-lowry-hole-in-one-players-championship-spt-intl/index.html",
    "https://www.cnn.com/2022/03/12/football/roman-abramovich-ukraine-russia-chelsea-fans-spt-intl/index.html",
    "https://www.cnn.com/2022/03/10/sport/ukraine-russia-putin-sports-sanctions-intl-spt/index.html",
    "https://www.cnn.com/2022/03/02/sport/oleksandr-usyk-ukraine-russia-invasion-boxing-spt-intl/index.html",
    "https://www.cnn.com/2022/03/14/football/messi-neymar-what-next-psg-spt-intl/index.html",
    "https://www.cnn.com/2022/03/12/sport/cristiano-ronaldo-806-goal-fifa-all-time-record-spt/index.html",
    "https://www.cnn.com/2022/03/04/sport/australian-cricketer-shane-warne-obituary-spt-intl/index.html",
    "https://www.cnn.com/2022/03/04/tennis/serena-williams-grand-slam-amanpour-spt-intl/index.html",
    "https://www.cnn.com/2022/02/25/golf/harold-varner-iii-gotm-spc-spt-intl/index.html",
    "https://www.cnn.com/2022/02/22/tennis/coco-gauff-tennis-serena-williams-spt-intl/index.html",
    "https://www.cnn.com/2022/03/14/golf/nelly-korda-blood-clot-golf-spt-intl/index.html",
    "https://www.cnn.com/2022/03/12/golf/players-championship-storm-pga-tour-delay-spt-intl/index.html",
    "https://www.cnn.com/2022/03/11/golf/players-championship-opening-round-weather-spt-intl/index.html",
    "https://www.cnn.com/2022/03/14/football/andriy-yarmolenko-tears-scores-west-ham-spt-intl/index.html",
    "https://www.cnn.com/2022/03/13/football/chelsea-newcastle-abramovich-havertz-saudi-spt-intl/index.html",
    "https://www.cnn.com/2022/03/03/football/amilcar-djau-codjovi-ukraine-russia-spt-intl/index.html",
    "https://www.cnn.com/2022/03/11/tennis/nick-kyrgios-indian-wells-spt-intl/index.html",
    "https://www.cnn.com/2022/03/09/tennis/andy-murray-donate-prize-money-ukraine-spt-intl/index.html",
    "https://www.cnn.com/2022/03/09/tennis/novak-djokovic-indian-wells-covid-spt-intl/index.html",
    "https://www.cnn.com/2022/03/14/sport/tom-brady-supposed-final-touchdown-ball-auction-spt-intl/index.html",
    "https://www.cnn.com/2022/03/13/sport/tom-brady-returns-tampa-bay-buccaneers/index.html",
    "https://www.cnn.com/2022/03/13/sport/patrick-mahomes-brittany-matthews-married/index.html",
    "https://www.cnn.com/2022/03/12/motorsport/lewis-hamilton-pre-season-testing-mercedes-spt-intl/index.html",
    "https://www.cnn.com/2022/03/09/motorsport/nikita-mazepin-russian-f1-haas-fund-spt-intl/index.html",
    "https://www.cnn.com/2022/03/03/motorsport/max-verstappen-red-bull-racing-contract-spt-intl/index.html",
    "https://www.cnn.com/2022/02/21/sport/winter-olympics-elite-wealthy-intl-spt/index.html",
    "https://www.cnn.com/2022/02/19/sport/kamila-valieva-eileen-gu-future-olympics-spt-intl/index.html",
    "https://www.cnn.com/2022/02/19/sport/olympic-athlete-cookbook-purple-project-spt-intl/index.html",
    "https://www.cnn.com/2022/02/21/sport/medina-spirit-kentucky-derby-win-disqualified/index.html",
    "https://www.cnn.com/2021/12/02/sport/chris-caserta-jockey-spt-intl/index.html",
    "https://www.cnn.com/2021/06/05/sport/essential-quality-belmont-stakes-winner/index.html",
    "https://www.cnn.com/2021/11/12/sport/lor-sabourin-climbing-identity-cmd-spt-intl/index.html",
    "https://www.cnn.com/2021/06/16/sport/nadhira-alharthy-profile-cmd-spt-intl/index.html",
    "https://www.cnn.com/2021/06/03/sport/janja-garnbret-climbing-olympics-tokyo-cmd-spt-intl/index.html",
    "https://www.cnn.com/2022/03/05/business/ukraine-war-hits-africa-lgs-cmd-intl/index.html",
    "https://www.cnn.com/2022/03/03/europe/international-students-trapped-sumy-ukraine-lgs-intl/index.html",
    "https://www.cnn.com/2022/02/28/europe/students-allege-racism-ukraine-cmd-intl/index.html",
    "https://www.cnn.com/2022/03/01/africa/africa-condemns-racism-ukraine-intl/index.html",
    "https://www.cnn.com/2022/02/23/europe/kenya-ukraine-russia-colonialism-intl/index.html",
    "https://www.cnn.com/2021/12/22/africa/south-africa-omicron-peak-intl/index.html",
    "https://www.cnn.com/2021/12/22/africa/south-africa-omicron-peak-intl/index.html",
    "https://www.cnn.com/2021/09/12/africa/africa-coups-resurgence-intl-cmd/index.html",
    "https://www.cnn.com/2021/09/12/africa/africa-coups-resurgence-intl-cmd/index.html",
    "https://www.cnn.com/2021/12/21/africa/solhan-burkina-faso-massacre-intl-cmd/index.html",
    "https://www.cnn.com/2022/02/06/football/senegal-africa-cup-of-nations-egypt/index.html",
    "https://www.cnn.com/2022/02/06/football/senegal-africa-cup-of-nations-egypt/index.html",
    "https://www.cnn.com/2022/01/29/sport/joel-embiid-cameroon-afcon-football-76ers-spt-intl/index.html",
    "https://www.cnn.com/2021/12/09/health/black-fetus-medical-illustration-diversity-wellness-cec/index.html",
    "https://www.cnn.com/2021/12/09/health/black-fetus-medical-illustration-diversity-wellness-cec/index.html",
    "https://www.cnn.com/2021/11/18/africa/ghana-green-bonds-sustainability-business-mpa-spc-intl/index.html",
    "https://www.cnn.com/2021/11/18/africa/ghana-green-bonds-sustainability-business-mpa-spc-intl/index.html",
    "https://www.cnn.com/2021/09/23/africa/coldhubs-nigeria-food-supply-chain-hnk-spc-intl/index.html",
    "https://www.cnn.com/2021/09/23/africa/coldhubs-nigeria-food-supply-chain-hnk-spc-intl/index.html",
    "https://www.cnn.com/2021/12/15/sport/masai-ujiri-nba-african-president-only-one-spc-intl/index.html",
    "https://www.cnn.com/2021/12/15/sport/masai-ujiri-nba-african-president-only-one-spc-intl/index.html",
    "https://www.cnn.com/2021/11/03/sport/chess-grandmasters-africa-spc-intl/index.html",
    "https://www.cnn.com/2022/02/15/africa/amapiano-south-africa-music-genre-origins-spc-intl/index.html",
    "https://www.cnn.com/2022/02/15/africa/amapiano-south-africa-music-genre-origins-spc-intl/index.html",
    "https://www.cnn.com/2021/09/22/africa/nigeria-ogbuagu-board-game-creator-spc-intl/index.html",
    "https://www.cnn.com/2022/01/13/health/chidiebere-ibe-medical-illustrations-published-nigeria-spc-intl/index.html",
    "https://www.cnn.com/2022/01/13/health/chidiebere-ibe-medical-illustrations-published-nigeria-spc-intl/index.html",
    "https://www.cnn.com/2022/03/09/africa/amazon-prime-video-nollywood-anthill-inkblot-spc-intl/index.html",
    "https://www.cnn.com/2022/03/09/africa/amazon-prime-video-nollywood-anthill-inkblot-spc-intl/index.html",
    "https://www.cnn.com/2022/03/01/africa/opibus-kenya-electric-mobility-bus-motorcycle-car-spc-intl/index.html",
    "https://www.cnn.com/2021/11/03/business/nigeria-clean-energy-transition/index.html",
    "https://www.cnn.com/2021/11/03/business/nigeria-clean-energy-transition/index.html",
    "https://www.cnn.com/2020/01/07/asia/fukushima-wildlife-intl-scli-scn/index.html",
    "https://www.cnn.com/2020/12/03/tech/autox-robotaxi-china-intl-hnk/index.html",
    "https://www.cnn.com/2022/03/15/asia/australia-climate-court-appeal-intl-hnk/index.html",
    "https://www.cnn.com/2022/03/15/asia/australia-climate-court-appeal-intl-hnk/index.html"
]


# Write the URLs to a CSV file
with open('input.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for url in urls:
        writer.writerow([url])

print("CSV file 'input.csv' has been created.")
