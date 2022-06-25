def loader(engine, tname, tvals, func='replace'):
    tvals.to_sql(name=tname, con=engine, if_exists=func, index=False)
