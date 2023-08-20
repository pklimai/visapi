
void get_geometry_json(
        int period_number = 7, 
        int run_number = 2076, 
        char* filepath = (char*) "/lhep/users/pklimai/geometry_run_7-2076.root") 
{

    cout << "I have inputs: " << period_number << " and " << run_number << endl;

    int res_code = UniRun::ReadGeometryFile(period_number, run_number, (char*)filepath);
    if (res_code != 0)
    {
        cout << "\nMacro finished with errors" << endl;
        exit(-1);
    }

    // get gGeoManager from ROOT file (if required)
    TFile* geoFile = new TFile(filepath, "READ");
    if (!geoFile->IsOpen())
    {
        cout<<"ERROR: could not open ROOT file with geometry!"<<endl;
        exit(-2);
    }

    TList* keyList = geoFile->GetListOfKeys();
    TIter next(keyList);
    TKey* key = (TKey*)next();
    TString className(key->GetClassName());
    if (className.BeginsWith("TGeoManager"))
        key->ReadObj();
    else
    {
        cout<<"ERROR: TGeoManager isn't top element in given file "<<filepath<<endl;
        exit(-3);
    }

    TGeoNode* N = gGeoManager->GetTopNode();
    cout<<"The top node of gGeoManager is "<<N->GetName()<<endl;

    TGeoManager *tgm = gGeoManager;
    cout << tgm;

    TString tgmjson = TBufferJSON::ToJSON(tgm);
    cout << tgmjson;

}

